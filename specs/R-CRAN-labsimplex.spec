%global __brp_check_rpaths %{nil}
%global packname  labsimplex
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Simplex Optimization Algorithms for Laboratory and ManufacturingProcesses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-scatterplot3d >= 0.3.41
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-scatterplot3d >= 0.3.41
Requires:         R-CRAN-ggplot2 

%description
Simplex optimization algorithms as firstly proposed by Spendley et al.
(1962) <doi:10.1080/00401706.1962.10490033> and later modified by Nelder
and Mead (1965) <doi:10.1093/comjnl/7.4.308> for laboratory and
manufacturing processes. The package also provides tools for graphical
representation of the simplexes and some example response surfaces that
are useful in illustrating the optimization process.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
