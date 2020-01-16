%global packname  cvmdisc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Cramer von Mises Tests for Discrete or Grouped Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-stats4 
Requires:         R-CRAN-CompQuadForm 

%description
Implements Cramer-von Mises Statistics for testing fit to (1) fully
specified discrete distributions as described in Choulakian, Lockhart and
Stephens (1994) <doi:10.2307/3315828> (2) discrete distributions with
unknown parameters that must be estimated from the sample data, see
Spinelli & Stephens (1997) <doi:10.2307/3315735> and Lockhart, Spinelli
and Stephens (2007) <doi:10.1002/cjs.5550350111> (3) grouped continuous
distributions with Unknown Parameters, see Spinelli (2001)
<doi:10.2307/3316040>. Maximum likelihood estimation (MLE) is used to
estimate the parameters. The package computes the Cramer-von Mises
Statistics, Anderson-Darling Statistics and the Watson-Stephens Statistics
and their p-values.

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
%{rlibdir}/%{packname}/INDEX
