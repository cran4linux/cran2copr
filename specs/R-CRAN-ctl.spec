%global __brp_check_rpaths %{nil}
%global packname  ctl
%global packver   1.0.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Correlated Trait Locus Mapping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-qtl 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-qtl 

%description
Identification and network inference of genetic loci associated with
correlation changes in quantitative traits (called correlated trait loci,
CTLs). Arends et al. (2016) <doi:10.21105/joss.00087>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/README.txt
%doc %{rlibdir}/%{packname}/STATUS.txt
%doc %{rlibdir}/%{packname}/TODO.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
