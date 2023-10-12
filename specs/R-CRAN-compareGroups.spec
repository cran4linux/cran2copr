%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  compareGroups
%global packver   4.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Descriptive Analysis by Groups

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-HardyWeinberg 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
Requires:         R-CRAN-survival 
Requires:         R-tools 
Requires:         R-CRAN-HardyWeinberg 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-methods 
Requires:         R-CRAN-chron 
Requires:         R-stats 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 

%description
Create data summaries for quality control, extensive reports for exploring
data, as well as publication-ready univariate or bivariate tables in
several formats (plain text, HTML,LaTeX, PDF, Word or Excel. Create
figures to quickly visualise the distribution of your data (boxplots,
barplots, normality-plots, etc.). Display statistics (mean, median,
frequencies, incidences, etc.). Perform the appropriate tests (t-test,
Analysis of variance, Kruskal-Wallis, Fisher, log-rank, ...) depending on
the nature of the described variable (normal, non-normal or qualitative).
Summarize genetic data (Single Nucleotide Polymorphisms) data displaying
Allele Frequencies and performing Hardy-Weinberg Equilibrium tests among
other typical statistics and tests for these kind of data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
