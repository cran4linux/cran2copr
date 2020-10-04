%global packname  boussinesq
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Analytic Solutions for (ground-water) Boussinesq Equation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
This package is a collection of R functions implemented from published and
available analytic solutions for the One-Dimensional Boussinesq Equation
(ground-water). In particular, the function "beq.lin" is the analytic
solution of the linearized form of Boussinesq Equation between two
different head-based boundary (Dirichlet) conditions; "beq.song" is the
non-linear power-series analytic solution of the motion of a wetting front
over a dry bedrock (Song at al, 2007, see complete reference on function
documentation). Bugs/comments/questions/collaboration of any kind are
warmly welcomed.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/example1.R
%doc %{rlibdir}/%{packname}/example2.R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
