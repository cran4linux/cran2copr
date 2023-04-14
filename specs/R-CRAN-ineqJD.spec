%global __brp_check_rpaths %{nil}
%global packname  ineqJD
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Inequality Joint Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computes and decomposes Gini, Bonferroni and Zenga 2007 point and
synthetic concentration indexes. Decompositions are intended: by sources,
by subpopulations and by sources and subpopulations jointly. References,
Zenga M. M.(2007) <doi:10.1400/209575> Zenga M. (2015)
<doi:10.1400/246627> Zenga M., Valli I. (2017)
<doi:10.26350/999999_000005> Zenga M., Valli I. (2018)
<doi:10.26350/999999_000011>.

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
