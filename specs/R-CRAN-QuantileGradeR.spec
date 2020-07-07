%global packname  QuantileGradeR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Quantile-Adjusted Restaurant Grading

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Implementation of the food safety restaurant grading system adopted by
Public Health - Seattle & King County (see Ashwood, Z.C., Elias, B., and
Ho. D.E. "Improving the Reliability of Food Safety Disclosure: A Quantile
Adjusted Restaurant Grading System for Seattle-King County" (working
paper)). As reported in the accompanying paper, this package allows
jurisdictions to easily implement refinements that address common
challenges with unadjusted grading systems. First, in contrast to
unadjusted grading, where the most recent single routine inspection is the
primary determinant of a grade, grading inputs are allowed to be flexible.
For instance, it is straightforward to base the grade on average
inspection scores across multiple inspection cycles. Second, the package
can identify quantile cutoffs by inputting substantively meaningful
regulatory thresholds (e.g., the proportion of establishments receiving
sufficient violation points to warrant a return visit). Third, the
quantile adjustment equalizes the proportion of establishments in a
flexible number of grading categories (e.g., A/B/C) across areas (e.g.,
ZIP codes, inspector areas) to account for inspector differences. Fourth,
the package implements a refined quantile adjustment that addresses two
limitations with the stats::quantile() function when applied to inspection
score datasets with large numbers of score ties. The quantile adjustment
algorithm iterates over quantiles until, over all restaurants in all
areas, grading proportions are within a tolerance of desired global
proportions. In addition the package allows a modified definition of
"quantile" from "Nearest Rank". Instead of requiring that at least p[1]%
of restaurants receive the top grade and at least (p[1]+p[2])% of
restaurants receive the top or second best grade for quantiles p, the
algorithm searches for cutoffs so that as close as possible p[1]% of
restaurants receive the top grade, and as close as possible to p[2]% of
restaurants receive the second top grade.

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
