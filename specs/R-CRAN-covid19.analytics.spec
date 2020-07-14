%global packname  covid19.analytics
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Load and Analyze Live Data from the CoViD-19 Pandemic

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-pheatmap 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-pheatmap 

%description
Load and analyze updated time series worldwide data of reported cases for
the Novel CoronaVirus Disease (CoViD-19) from the Johns Hopkins University
Center for Systems Science and Engineering (JHU CSSE) data repository
<https://github.com/CSSEGISandData/COVID-19>. The datasets are available
in two main modalities, as a time series sequences and aggregated for the
last day with greater spatial resolution. Several analysis, visualization
and modelling functions are available in the package that will allow the
user to compute and visualize total number of cases, total number of
changes and growth rate globally or for an specific geographical location,
while at the same time generating models using these trends; generate
interactive visualizations and generate Susceptible-Infected-Recovered
(SIR) model for the disease spread.

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
