%global packname  phylosim
%global packver   3.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.4
Release:          1%{?dist}
Summary:          Flexible Simulations of Biological Sequence Evolution

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 2.3
BuildRequires:    R-CRAN-R.oo >= 1.13.0
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-CRAN-compoisson >= 0.3
BuildRequires:    R-CRAN-R.methodsS3 
Requires:         R-CRAN-ape >= 2.3
Requires:         R-CRAN-R.oo >= 1.13.0
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-CRAN-compoisson >= 0.3
Requires:         R-CRAN-R.methodsS3 

%description
An extensible object-oriented framework for the Monte Carlo simulation of
sequence evolution written in 100 percent R. It is built on the top of the
R.oo and ape packages and uses Gillespie's direct method to simulate
substitutions, insertions and deletions. Citation: Botond Sipos, Tim
Massingham, Gregory E Jordan and Nick Goldman (2011) PhyloSim - Monte
Carlo simulation of sequence evolution in the R statistical computing
environment <doi:10.1186/1471-2105-12-104>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
