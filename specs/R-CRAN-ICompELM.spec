%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICompELM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Independent Component Analysis Based Extreme Learning Machine

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-CRAN-ica 
Requires:         R-stats 
Requires:         R-CRAN-tsutils 
Requires:         R-CRAN-ica 

%description
Single Layer Feed-forward Neural networks (SLFNs) have many applications
in various fields of statistical modelling, especially for time-series
forecasting. However, there are some major disadvantages of training such
networks via the widely accepted 'gradient-based backpropagation'
algorithm, such as convergence to local minima, dependencies on learning
rate and large training time. These concerns were addressed by Huang et
al. (2006) <doi:10.1016/j.neucom.2005.12.126>, wherein they introduced the
Extreme Learning Machine (ELM), an extremely fast learning algorithm for
SLFNs which randomly chooses the weights connecting input and hidden nodes
and analytically determines the output weights of SLFNs. It shows good
generalized performance, but is still subject to a high degree of
randomness. To mitigate this issue, this package uses a dimensionality
reduction technique given in Hyvarinen (1999) <doi:10.1109/72.761722>,
namely, the Independent Component Analysis (ICA) to determine the
input-hidden connections and thus, remove any sort of randomness from the
algorithm. This leads to a robust, fast and stable ELM model. Using
functions within this package, the proposed model can also be compared
with an existing alternative based on the Principal Component Analysis
(PCA) algorithm given by Pearson (1901) <doi:10.1080/14786440109462720>,
i.e., the PCA based ELM model given by Castano et al. (2013)
<doi:10.1007/s11063-012-9253-x>, from which the implemented ICA based
algorithm is greatly inspired.

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
