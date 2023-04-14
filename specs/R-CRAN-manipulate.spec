%global __brp_check_rpaths %{nil}
%global packname  manipulate
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Plots for RStudio

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch

%description
Interactive plotting functions for use within RStudio. The manipulate
function accepts a plotting expression and a set of controls (e.g. slider,
picker, checkbox, or button) which are used to dynamically change values
within the expression. When a value is changed using its corresponding
control the expression is automatically re-executed and the plot is
redrawn.

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
