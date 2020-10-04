%global packname  HMMextra0s
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Hidden Markov Models with Extra Zeros

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ellipse 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ellipse 

%description
Contains functions for hidden Markov models with observations having extra
zeros as defined in the following two publications, Wang, T., Zhuang, J.,
Obara, K. and Tsuruoka, H. (2016) <doi:10.1111/rssc.12194>; Wang, T.,
Zhuang, J., Buckby, J., Obara, K. and Tsuruoka, H. (2018)
<doi:10.1029/2017JB015360>. The observed response variable is either
univariate or bivariate Gaussian conditioning on presence of events, and
extra zeros mean that the response variable takes on the value zero if
nothing is happening. Hence the response is modelled as a mixture
distribution of a Bernoulli variable and a continuous variable. That is,
if the Bernoulli variable takes on the value 1, then the response variable
is Gaussian, and if the Bernoulli variable takes on the value 0, then the
response is zero too. This package includes functions for simulation,
parameter estimation, goodness-of-fit, the Viterbi algorithm, and plotting
the classified 2-D data. Some of the functions in the package are based on
those of the R package 'HiddenMarkov' by David Harte.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
