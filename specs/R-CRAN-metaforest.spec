%global packname  metaforest
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Exploring Heterogeneity in Meta-Analysis using Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-gtable 
Requires:         R-grid 

%description
Conduct random forests-based meta-analysis, obtain partial dependence
plots for metaforest and classic meta-analyses, and cross-validate and
tune metaforest- and classic meta-analyses in conjunction with the caret
package. A requirement of classic meta-analysis is that the studies being
aggregated are conceptually similar, and ideally, close replications.
However, in many fields, there is substantial heterogeneity between
studies on the same topic. Classic meta-analysis lacks the power to assess
more than a handful of univariate moderators. MetaForest, by contrast, has
substantial power to explore heterogeneity in meta-analysis. It can
identify important moderators from a larger set of potential candidates,
even with as little as 20 studies (Van Lissa, in preparation). This is an
appealing quality, because many meta-analyses have small sample sizes.
Moreover, MetaForest yields a measure of variable importance which can be
used to identify important moderators, and offers partial prediction plots
to explore the shape of the marginal relationship between moderators and
effect size.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
