%global packname  MVTests
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Multivariate Hypothesis Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 

%description
Multivariate hypothesis tests and the confidence intervals. This package
can be used for hypothesis tests which are The Hotelling T Square Tests
(One-Sample, Two Independent Samples, Paired Samples), The One Way
MANOVA,The Multivariate Shapiro-Wilk Test for Multivariate Normality Test,
The Bartlett Test for One Sample Covariance Matrix, The Box-M Test and The
Bartlett's Sphericity Test. For this package, we have benefited the
studies Rencher (2003), Nel and Merwe (1986) <DOI:
10.1080/03610928608829342>, Tatlidil (1996), James (1994) <DOI:
10.2307/2333003>, Tsagris (2014), Villasenor Alva and Estrada (2009) <DOI:
10.1080/03610920802474465>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
