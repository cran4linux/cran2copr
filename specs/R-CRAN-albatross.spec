%global packname  albatross
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          PARAFAC Analysis of Fluorescence Excitation-Emission Matrices

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-multiway >= 1.0.4
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-lattice 
Requires:         R-CRAN-multiway >= 1.0.4
Requires:         R-CRAN-pracma 
Requires:         R-lattice 

%description
Perform parallel factor analysis (PARAFAC: Harshman, 2005)
<doi:10.1121/1.1977523>) on fluorescence excitation-emission matrices
(FEEMs): handle scattering signal (Bahram, 2007) <doi:10.1002/cem.978> and
inner filter effect (Kothawala, 2013) <doi:10.4319/lom.2013.11.616>, scale
the dataset, fit the model; perform split-half validation (DeSarbo, 1984)
<https://papers.ssrn.com/abstract=2783446> or jack-knifing (Riu, 2003)
<doi:10.1016/S0169-7439(02)00090-4>. The package has a low dependency
footprint (only two direct dependencies not in core or recommended; four
total non-core/recommended dependencies) and has been tested on a wide
range of R versions (including R as old as 3.3.3 from Debian Stretch).

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
