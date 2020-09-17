%global packname  gmGeostats
%global packver   0.10-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.6
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistics for Compositional Analysis

License:          CC BY-SA 4.0 | GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-compositions >= 2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-compositions >= 2.0
Requires:         R-methods 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-boot 
Requires:         R-CRAN-foreach 
Requires:         R-utils 
Requires:         R-CRAN-RColorBrewer 

%description
Support for geostatistical analysis of multivariate data, in particular
data with restrictions, e.g. positive amounts data, compositional data,
distributional data, microstructural data, etc. It includes descriptive
analysis and modelling for such data, both from a two-point Gaussian
perspective and multipoint perspective. The methods mainly follow
Tolosana-Delgado, Mueller and van den Boogaart (2018)
<doi:10.1007/s11004-018-9769-3>.

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
