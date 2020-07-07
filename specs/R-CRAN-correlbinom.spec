%global packname  correlbinom
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Correlated Binomial Probabilities

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rmpfr 
Requires:         R-methods 

%description
Calculates the probabilities of k successes given n trials of a binomial
random variable with non-negative correlation across trials. The function
takes as inputs the scalar values the level of correlation or association
between trials, the success probability, the number of trials, an optional
input specifying the number of bits of precision used in the calculation,
and an optional input specifying whether the calculation approach to be
used is from Witt (2014) <doi:10.1080/03610926.2012.725148> or from Kuk
(2004) <doi:10.1046/j.1467-9876.2003.05369.x>. The output is a
(trials+1)-dimensional vector containing the likelihoods of 0, 1, ...,
trials successes.

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
