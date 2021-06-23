%global __brp_check_rpaths %{nil}
%global packname  SADISA
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Species Abundance Distributions with Independent-SpeciesAssumption

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-DDD >= 4.1
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-DDD >= 4.1
Requires:         R-CRAN-pracma 

%description
Computes the probability of a set of species abundances of a single or
multiple samples of individuals with one or more guilds under a
mainland-island model. One must specify the mainland (metacommunity) model
and the island (local) community model. It assumes that species fluctuate
independently. The package also contains functions to simulate under this
model. See Haegeman, B. & R.S. Etienne (2017). A general sampling formula
for community structure data. Methods in Ecology & Evolution 8: 1506-1519
<doi:10.1111/2041-210X.12807>.

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

%files
%{rlibdir}/%{packname}
