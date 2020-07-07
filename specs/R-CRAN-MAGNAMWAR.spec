%global packname  MAGNAMWAR
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          A Pipeline for Meta-Genome Wide Association

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-qqman 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-seqinr 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-multcomp 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-qqman 
Requires:         R-survival 
Requires:         R-CRAN-seqinr 

%description
Correlates variation within the meta-genome to target species phenotype
variations in meta-genome with association studies. Follows the pipeline
described in Chaston, J.M. et al. (2014) <doi:10.1128/mBio.01631-14>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
