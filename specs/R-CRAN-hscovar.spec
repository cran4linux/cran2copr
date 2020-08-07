%global packname  hscovar
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Calculation of Covariance Between Markers for Half-Sib Families

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-pwr 
Requires:         R-parallel 
Requires:         R-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-pwr 

%description
The theoretical covariance between pairs of markers is calculated from
either paternal haplotypes and maternal linkage disequilibrium (LD) or
vise versa. A genetic map is required. Grouping of markers is based on the
correlation matrix and a representative marker is suggested for each
group. Employing the correlation matrix, optimal sample size can be
derived for association studies based on a SNP-BLUP approach. The
implementation relies on paternal half-sib families and biallelic markers.
If maternal half-sib families are used, the roles of sire/dam are swapped.
Multiple families can be considered. Wittenburg, Bonk, Doschoris, Reyer
(2019) "Design of Experiments for Fine-Mapping Quantitative Trait Loci in
Livestock Populations" <doi:10.1101/2019.12.17.879106>. Carlson, Eberle,
Rieder, Yi, Kruglyak, Nickerson (2004) "Selecting a maximally informative
set of single-nucleotide polymorphisms for association analyses using
linkage disequilibrium" <doi:10.1086/381000>.

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
