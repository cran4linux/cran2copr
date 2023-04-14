%global __brp_check_rpaths %{nil}
%global packname  Rarity
%global packver   1.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.6
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Rarity Indices for Species and Assemblages ofSpecies

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Allows calculation of rarity weights for species and indices of rarity for
assemblages of species according to different methods (Leroy et al. 2012,
Insect. Conserv. Divers. 5:159-168 <doi:10.1111/j.1752-4598.2011.00148.x>;
Leroy et al. 2013, Divers. Distrib. 19:794-803 <doi:10.1111/ddi.12040>).

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
