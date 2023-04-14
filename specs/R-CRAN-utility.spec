%global __brp_check_rpaths %{nil}
%global packname  utility
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          3%{?dist}%{?buildtag}
Summary:          Construct, Evaluate and Plot Value and Utility Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Construct and plot objective hierarchies and associated value and utility
functions. Evaluate the values and utilities and visualize the results as
colored objective hierarchies or tables. Visualize uncertainty by plotting
median and quantile intervals within the nodes of objective hierarchies.
Get numerical results of the evaluations in standard R data types for
further processing.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
