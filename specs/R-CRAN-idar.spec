%global packname  idar
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Individual Diversity-Area Relationships

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-FD 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-ape 

%description
Computes and tests individual (species, phylogenetic and functional)
diversity-area relationships, i.e., how species-, phylogenetic- and
functional-diversity varies with spatial scale around the individuals of
some species in a community. See applications of these methods in Wiegand
et al. (2007) <doi:10.1073/pnas.0705621104> or Chacon-Labella et al.
(2016) <doi:10.1007/s00442-016-3547-z>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
