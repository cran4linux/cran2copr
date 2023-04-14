%global __brp_check_rpaths %{nil}
%global packname  optextras
%global packver   2019-12.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2019.12.4
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Support Optimization Possibly with Bounds and Masks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 

%description
Tools to assist in safely applying user generated objective and derivative
function to optimization programs. These are primarily function
minimization methods with at most bounds and masks on the parameters.
Provides a way to check the basic computation of objective functions that
the user provides, along with proposed gradient and Hessian functions, as
well as to wrap such functions to avoid failures when inadmissible
parameters are provided. Check bounds and masks. Check scaling or
optimality conditions. Perform an axial search to seek lower points on the
objective function surface. Includes forward, central and backward
gradient approximation codes.

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
