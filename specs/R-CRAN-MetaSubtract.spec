%global __brp_check_rpaths %{nil}
%global packname  MetaSubtract
%global packver   1.60
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.60
Release:          3%{?dist}%{?buildtag}
Summary:          Subtracting Summary Statistics of One or more Cohorts fromMeta-GWAS Results

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
If results from a meta-GWAS are used for validation in one of the cohorts
that was included in the meta-analysis, this will yield biased (i.e. too
optimistic) results. The validation cohort needs to be independent from
the meta-Genome-Wide-Association-Study (meta-GWAS) results. 'MetaSubtract'
will subtract the results of the respective cohort from the meta-GWAS
results analytically without having to redo the meta-GWAS analysis using
the leave-one-out methodology. It can handle different meta-analyses
methods and takes into account if single or double genomic control
correction was applied to the original meta-analysis. It can also handle
different meta-analysis methods. It can be used for whole GWAS, but also
for a limited set of genetic markers. See for application: Nolte I.M. et
al. (2017); <doi: 10.1038/ejhg.2017.50>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
