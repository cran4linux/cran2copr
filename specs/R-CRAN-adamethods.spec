%global packname  adamethods
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Archetypoid Algorithms and Anomaly Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Anthropometry 
BuildRequires:    R-CRAN-archetypes 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tolerance 
BuildRequires:    R-CRAN-univOutl 
BuildRequires:    R-utils 
Requires:         R-CRAN-Anthropometry 
Requires:         R-CRAN-archetypes 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-nnls 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-tolerance 
Requires:         R-CRAN-univOutl 
Requires:         R-utils 

%description
Collection of several algorithms to obtain archetypoids with small and
large databases, and with both classical multivariate data and functional
data (univariate and multivariate). Some of these algorithms also allow to
detect anomalies (outliers). Please see Vinue and Epifanio (2020)
<doi:10.1007/s11634-020-00412-9>.

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
