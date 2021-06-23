%global __brp_check_rpaths %{nil}
%global packname  DesignCTPB
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Design Clinical Trials with Potential Biomarker Effect

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotly 

%description
Applying 'CUDA' 'GPUs' via 'Numba' for optimal clinical design. It allows
the user to utilize a 'reticulate' 'Python' environment and run intensive
Monte Carlo simulation to get the optimal cutoff for the clinical design
with potential biomarker effect, which can guide the realistic clinical
trials.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
