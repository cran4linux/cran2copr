%global packname  scdhlm
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}
Summary:          Estimating Hierarchical Linear Models for Single-Case Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-stats 
Requires:         R-nlme 
Requires:         R-stats 

%description
Provides a set of tools for estimating hierarchical linear models and
effect sizes based on data from single-case designs. Functions are
provided for calculating standardized mean difference effect sizes that
are directly comparable to standardized mean differences estimated from
between-subjects randomized experiments, as described in Hedges,
Pustejovsky, and Shadish (2012) <DOI:10.1002/jrsm.1052>; Hedges,
Pustejovsky, and Shadish (2013) <DOI:10.1002/jrsm.1086>; and Pustejovsky,
Hedges, and Shadish (2014) <DOI:10.3102/1076998614547577>. Includes an
interactive web interface.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
