Summary:	SCIM Array 30 Input Method Engine
Summary(pl.UTF-8):	Silnik metody wprowadzania Array 30 dla SCIM
Summary(zh_TW.UTF-8):	SCIM 行列 30 輸入法引擎
Name:		scim-array
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://of.openfoundry.org/download_path/scimarray/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	689a49455f3c868182aa00310b0e5c29
URL:		http://scimarray.openfoundry.org/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.4.0
Requires:	scim >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM Array 30 Input Method Engine provides with all the functions of
Array 30, including 1st and 2nd level short codes, special codes, and
symbol input.

%description -l pl.UTF-8
Silnik metody wprowadzania znaków Array 30 dla SCIM udostępnia
wszystkie funkcje Array 30, w tym kody krótkie poziomu 1. i 2., kody
specjalne oraz wprowadzanie symboli.

%description -l zh_TW.UTF-8
scim-array 為 SCIM 輸入法框架中完整實作行列 30 輸入法功能的輸入法引擎模組，
支援一級簡碼、二級簡碼、特別碼、符號輸入等功能，並和 OpenVanilla 中之行列輸入法一樣
，提供特別碼的提示和特行模式。scim-array 為自由軟體，採 GPL 授權方式釋出。

特點
 - 支援行列 6.0 Unicode 字碼表，可輸入Unicode Ext.A 及 Ext.B 中日韓漢字
 - 支援一級簡碼及二級簡碼
 - 支援特別碼輸入
 - 具有特別碼提示功能， 可幫助記憶特別碼
 - 具有特行模式，強迫使用特別碼輸入， 以提升打字速度
 - 完整 SCIM 支援，使用 SCIM 內建函式庫進行開發，無需另裝其它函式庫或輸入法框架

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/1.4.0/IMEngine/array.so
%attr(755,root,root) %{_libdir}/scim-1.0/1.4.0/SetupUI/array-imengine-setup.so
%{_datadir}/scim/Array
%{_datadir}/scim/icons/scim-array.png
