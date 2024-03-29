%global __brp_check_rpaths %{nil}
%global packname  bootLR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrapped Confidence Intervals for (Negative) LikelihoodRatio Tests

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-binom 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-CRAN-binom 

%description
Computes appropriate confidence intervals for the likelihood ratio tests
commonly used in medicine/epidemiology, using the method of Marill et al.
(2015) <doi:10.1177/0962280215592907>.  It is particularly useful when the
sensitivity or specificity in the sample is 100%.  Note that this does not
perform the test on nested models--for that, see 'epicalc::lrtest'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
