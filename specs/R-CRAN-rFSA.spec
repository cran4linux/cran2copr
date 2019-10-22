%global packname  rFSA
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Feasible Solution Algorithm for Finding Best Subsets andInteractions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-hashmap 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
Requires:         R-parallel 
Requires:         R-CRAN-hashmap 
Requires:         R-methods 
Requires:         R-CRAN-tibble 

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
