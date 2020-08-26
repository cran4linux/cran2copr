%global packname  unikn
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Elements of the University of Konstanz's CorporateDesign

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 

%description
Define and use graphical elements of corporate design manuals in R. The
'unikn' package provides color functions (by defining dedicated colors and
color palettes, and commands for changing, viewing, and using them) and
styled text elements (e.g., for marking, underlining, or plotting colored
titles). The pre-defined range of colors and text functions is based on
the corporate design of the University of Konstanz
<https://www.uni-konstanz.de/>, but can be adapted and extended for other
institutions and purposes.

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
