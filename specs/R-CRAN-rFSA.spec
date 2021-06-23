%global __brp_check_rpaths %{nil}
%global packname  rFSA
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          3%{?dist}%{?buildtag}
Summary:          Feasible Solution Algorithm for Finding Best Subsets andInteractions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rPref 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-hash 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rPref 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-hash 

%description
Assists in statistical model building to find optimal and semi-optimal
higher order interactions and best subsets. Uses the lm(), glm(), and
other R functions to fit models generated from a feasible solution
algorithm. Discussed in Subset Selection in Regression, A Miller (2002).
Applied and explained for least median of squares in Hawkins (1993)
<doi:10.1016/0167-9473(93)90246-P>. The feasible solution algorithm comes
up with model forms of a specific type that can have fixed variables,
higher order interactions and their lower order terms.

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
%{rlibdir}/%{packname}/INDEX
