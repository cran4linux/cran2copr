%global __brp_check_rpaths %{nil}
%global packname  haldensify
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Highly Adaptive Lasso Conditional Density Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-origami >= 1.0.3
BuildRequires:    R-CRAN-hal9001 >= 0.2.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-origami >= 1.0.3
Requires:         R-CRAN-hal9001 >= 0.2.5
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Rdpack 

%description
Conditional density estimation is a longstanding and challenging problem
in statistical theory, and numerous proposals exist for optimally
estimating such complex functions. Algorithms for nonparametric estimation
of conditional densities based on a pooled hazard regression formulation
and semiparametric estimation via conditional hazards modeling are
implemented based on the highly adaptive lasso, a nonparametric regression
function for efficient estimation with fast convergence under mild
assumptions. The pooled hazards formulation implemented was first
described by Díaz and van der Laan (2011) <doi:10.2202/1557-4679.1356>.

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
