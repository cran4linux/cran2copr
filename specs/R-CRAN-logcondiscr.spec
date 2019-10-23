%global packname  logcondiscr
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Estimate a Log-Concave Probability Mass Function from Discretei.i.d. Observations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cobs 
Requires:         R-stats 

%description
Given independent and identically distributed observations X(1), ...,
X(n), allows to compute the maximum likelihood estimator (MLE) of
probability mass function (pmf) under the assumption that it is
log-concave, see Weyermann (2007) and Balabdaoui, Jankowski, Rufibach, and
Pavlides (2012). The main functions of the package are 'logConDiscrMLE'
that allows computation of the log-concave MLE, 'logConDiscrCI' that
computes pointwise confidence bands for the MLE, and
'kInflatedLogConDiscr' that computes a mixture of a log-concave PMF and a
point mass at k.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
