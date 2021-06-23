%global __brp_check_rpaths %{nil}
%global packname  PublicationBias
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis for Publication Bias in Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-robumeta 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-MetaUtility 
Requires:         R-CRAN-metafor 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-robumeta 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-MetaUtility 

%description
Performs sensitivity analysis for publication bias in meta-analyses (per
Mathur & VanderWeele, 2020 [<https://osf.io/s9dp6>]). These analyses
enable statements such as: "For publication bias to shift the observed
point estimate to the null, 'significant' results would need to be at
least 30-fold more likely to be published than negative or
'nonsignificant' results." Comparable statements can be made regarding
shifting to a chosen non-null value or shifting the confidence interval.
Provides a worst-case meta-analytic point estimate under maximal
publication bias obtained simply by conducting a standard meta-analysis of
only the negative and "nonsignificant" studies.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
