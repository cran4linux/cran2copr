%global __brp_check_rpaths %{nil}
%global packname  rPref
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Database Preferences and Skyline Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-RcppParallel >= 4.3.6
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-lazyeval >= 0.2.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-RcppParallel >= 4.3.6
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-lazyeval >= 0.2.1
Requires:         R-methods 
Requires:         R-utils 

%description
Routines to select and visualize the maxima for a given strict partial
order. This especially includes the computation of the Pareto frontier,
also known as (Top-k) Skyline operator (see Börzsönyi, et al. (2001)
<doi:10.1109/ICDE.2001.914855>), and some generalizations known as
database preferences (see Kießling (2002)
<doi:10.1016/B978-155860869-6/50035-4>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
