%global packname  cellVolumeDist
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Functions to fit cell volume distributions and thereby estimatecell growth rates and division times

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm >= 1.1.1
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-minpack.lm >= 1.1.1
Requires:         R-CRAN-gplots 

%description
This package implements a methodology for using cell volume distributions
to estimate cell growth rates and division times that is described in the
paper entitled "Cell Volume Distributions Reveal Cell Growth Rates and
Division Times", by Michael Halter, John T. Elliott, Joseph B. Hubbard,
Alessandro Tona and Anne L. Plant, which is in press in the Journal of
Theoretical Biology.  In order to reproduce the analysis used to obtain
Table 1 in the paper, execute the command "example(fitVolDist)".

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
