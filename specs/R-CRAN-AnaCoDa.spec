%global __brp_check_rpaths %{nil}
%global packname  AnaCoDa
%global packver   0.1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Codon Data under Stationarity using a Bayesian Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-CRAN-VGAM 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 

%description
Is a collection of models to analyze genome scale codon data using a
Bayesian framework. Provides visualization routines and checkpointing for
model fittings. Currently published models to analyze gene data for
selection on codon usage based on Ribosome Overhead Cost (ROC) are: ROC
(Gilchrist et al. (2015) <doi:10.1093/gbe/evv087>), and ROC with phi
(Wallace & Drummond (2013) <doi:10.1093/molbev/mst051>). In addition
'AnaCoDa' contains three currently unpublished models. The FONSE (First
order approximation On NonSense Error) model analyzes gene data for
selection on codon usage against of nonsense error rates. The PA (PAusing
time) and PANSE (PAusing time + NonSense Error) models use ribosome
footprinting data to analyze estimate ribosome pausing times with and
without nonsense error rate from ribosome footprinting data.

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
