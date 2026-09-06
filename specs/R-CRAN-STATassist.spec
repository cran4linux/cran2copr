%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  STATassist
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Standardised Statistical Comparison Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-utils 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-glmnet 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-Rtsne 
Requires:         R-stats 
Requires:         R-CRAN-umap 
Requires:         R-utils 

%description
Runs the applicable tests for a comparison in one call and returns
standardised result tables. One-sample, two-group, multi-group, factorial
and categorical workflows report parametric, rank-based and robust results
side by side with effect sizes, confidence intervals and
multiplicity-adjusted p-values. Supervised fits, embeddings, clustering
and simulators follow the same result contracts. Methods include those of
Welch (1947) <doi:10.1093/biomet/34.1-2.28>, Wilcoxon (1945)
<doi:10.2307/3001968>, Mann and Whitney (1947)
<doi:10.1214/aoms/1177730491>, Kruskal and Wallis (1952)
<doi:10.1080/01621459.1952.10483441>, Friedman (1937)
<doi:10.1080/01621459.1937.10503522>, Tukey (1949) <doi:10.2307/3001913>,
Dunn (1964) <doi:10.1080/00401706.1964.10490181>, Yuen (1974)
<doi:10.1093/biomet/61.1.165>, Brunner and Munzel (2000)
<doi:10.1002/(SICI)1521-4036(200001)42:1%%3C17::AID-BIMJ17%%3E3.0.CO;2-U>,
Algina, Keselman and Penfield (2005) <doi:10.1037/1082-989X.10.3.317>,
DeLong, DeLong and Clarke-Pearson (1988) <doi:10.2307/2531595>, Sun and Xu
(2014) <doi:10.1109/LSP.2014.2337313>, Pencina, D'Agostino, D'Agostino and
Vasan (2008) <doi:10.1002/sim.2929>, and Pencina, D'Agostino and
Steyerberg (2011) <doi:10.1002/sim.4085>.

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
