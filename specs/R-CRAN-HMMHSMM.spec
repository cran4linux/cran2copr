%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HMMHSMM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inference and Estimation of Hidden Markov Models and Hidden Semi-Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-extRemes 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-evd 
Requires:         R-CRAN-extRemes 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
Provides flexible maximum likelihood estimation and inference for Hidden
Markov Models (HMMs) and Hidden Semi-Markov Models (HSMMs), as well as the
underlying systems in which they operate. The package supports a wide
range of observation and dwell-time distributions, offering a flexible
modelling framework suitable for diverse practical data. Efficient
implementations of the forward-backward and Viterbi algorithms are
provided via 'Rcpp' for enhanced computational performance. Additional
functionality includes model simulation, residual analysis,
non-initialised estimation, local and global decoding, calculation of
diverse information criteria, computation of confidence intervals using
parametric bootstrap methods, numerical covariance matrix estimation, and
comprehensive visualisation functions for interpreting the data-generating
processes inferred from the models. Methods follow standard approaches
described by Guédon (2003) <doi:10.1198/1061860032030>, Zucchini and
MacDonald (2009, ISBN:9781584885733), and O'Connell and Højsgaard (2011)
<doi:10.18637/jss.v039.i04>.

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
