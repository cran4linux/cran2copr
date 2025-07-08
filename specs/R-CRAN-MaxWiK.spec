%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MaxWiK
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Method Based on Isolation Kernel Mean Embedding

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-abc 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-parallel 
Requires:         R-CRAN-abc 
Requires:         R-CRAN-ggplot2 

%description
Incorporates Approximate Bayesian Computation to get a posterior
distribution and to select a model optimal parameter for an observation
point. Additionally, the meta-sampling heuristic algorithm is realized for
parameter estimation, which requires no model runs and is
dimension-independent. A sampling scheme is also presented that allows
model runs and uses the meta-sampling for point generation. A predictor is
realized as the meta-sampling for the model output. All the algorithms
leverage a machine learning method utilizing the maxima weighted Isolation
Kernel approach, or 'MaxWiK'. The method involves transforming raw data to
a Hilbert space (mapping) and measuring the similarity between simulated
points and the maxima weighted Isolation Kernel mapping corresponding to
the observation point. Comprehensive details of the methodology can be
found in the papers Iurii Nagornov (2024)
<doi:10.1007/978-3-031-66431-1_16> and Iurii Nagornov (2023)
<doi:10.1007/978-3-031-29168-5_18>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
