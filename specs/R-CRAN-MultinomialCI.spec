%global packname  MultinomialCI
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Simultaneous Confidence Intervals for Multinomial ProportionsAccording to the Method by Sison and Glaz

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch

%description
An implementation of a method for building simultaneous confidence
intervals for the probabilities of a multinomial distribution given a set
of observations, proposed by Sison and Glaz in their paper: Sison, C.P and
J. Glaz. Simultaneous confidence intervals and sample size determination
for multinomial proportions. Journal of the American Statistical
Association, 90:366-369 (1995). The method is an R translation of the SAS
code implemented by May and Johnson in their paper: May, W.L. and W.D.
Johnson. Constructing two-sided simultaneous confidence intervals for
multinomial proportions for small counts in a large number of cells.
Journal of Statistical Software 5(6) (2000). Paper and code available at
<DOI:10.18637/jss.v005.i06>.

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
