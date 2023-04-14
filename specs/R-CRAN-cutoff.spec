%global __brp_check_rpaths %{nil}
%global packname  cutoff
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Seek the Significant Cutoff Value

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-set 
BuildRequires:    R-CRAN-do 
BuildRequires:    R-CRAN-ROCit 
Requires:         R-survival 
Requires:         R-CRAN-set 
Requires:         R-CRAN-do 
Requires:         R-CRAN-ROCit 

%description
Seek the significant cutoff value for a continuous variable, which will be
transformed into a classification, for linear regression, logistic
regression, logrank analysis and cox regression. First of all, all
combinations will be gotten by combn() function. Then n.per argument,
abbreviated of total number percentage, will be used to remove the
combination of smaller data group. In logistic, Cox regression and logrank
analysis, we will also use p.per argument, patient percentage, to filter
the lower proportion of patients in each group. Finally, p value in
regression results will be used to get the significant combinations and
output relevant parameters. In this package, there is no limit to the
number of cutoff points, which can be 1, 2, 3 or more. Still, we provide 2
methods, typical Bonferroni and Duglas G (1994) <doi:
10.1093/jnci/86.11.829>, to adjust the p value, Missing values will be
deleted by na.omit() function before analysis.

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
