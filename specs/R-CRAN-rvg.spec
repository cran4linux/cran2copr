%global __brp_check_rpaths %{nil}
%global packname  rvg
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          2%{?dist}%{?buildtag}
Summary:          R Graphics Devices for Vector Graphics Output

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-officer >= 0.3.6
BuildRequires:    R-CRAN-gdtools >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-officer >= 0.3.6
Requires:         R-CRAN-gdtools >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 

%description
Vector Graphics devices for Microsoft PowerPoint and Excel. Functions
extending package 'officer' are provided to embed 'DrawingML' graphics
into 'Microsoft PowerPoint' presentations and 'Microsoft Excel' workbooks.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
