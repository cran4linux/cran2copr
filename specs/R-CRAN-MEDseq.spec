%global __brp_check_rpaths %{nil}
%global packname  MEDseq
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mixtures of Exponential-Distance Models with Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3.0
BuildRequires:    R-CRAN-TraMineR >= 1.6
BuildRequires:    R-CRAN-matrixStats >= 0.53.1
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-seriation 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-WeightedCluster 
Requires:         R-CRAN-nnet >= 7.3.0
Requires:         R-CRAN-TraMineR >= 1.6
Requires:         R-CRAN-matrixStats >= 0.53.1
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-seriation 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-WeightedCluster 

%description
Implements a model-based clustering method for categorical life-course
sequences relying on mixtures of exponential-distance models introduced by
Murphy et al. (2021) <doi:10.1111/rssa.12712>. A range of flexible
precision parameter settings corresponding to weighted generalisations of
the Hamming distance metric are considered, along with the potential
inclusion of a noise component. Gating covariates can be supplied in order
to relate sequences to baseline characteristics. Sampling weights are also
accommodated. The models are fitted using the EM algorithm and tools for
visualising the results are also provided.

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
