%global packname  fasta
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fast Adaptive Shrinkage/Thresholding Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
A collection of acceleration schemes for proximal gradient methods for
estimating penalized regression parameters described in Goldstein, Studer,
and Baraniuk (2016) <arXiv:1411.3406>. Schemes such as Fast Iterative
Shrinkage and Thresholding Algorithm (FISTA) by Beck and Teboulle (2009)
<doi:10.1137/080716542> and the adaptive stepsize rule introduced in
Wright, Nowak, and Figueiredo (2009) <doi:10.1109/TSP.2009.2016892> are
included. You provide the objective function and proximal mappings, and it
takes care of the issues like stepsize selection, acceleration, and
stopping conditions for you.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
