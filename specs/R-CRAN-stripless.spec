%global packname  stripless
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Structured Trellis Displays Without Strips for Lattice Graphics

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
Requires:         R-utils 
Requires:         R-lattice 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 

%description
For making Trellis-type conditioning plots without strip labels. This is
useful for displaying the structure of results from factorial designs and
other studies when many conditioning variables would clutter the display
with layers of redundant strip labels. Settings of the variables are
encoded by layout and spacing in the trellis array and decoded by a
separate legend. The functionality is implemented by a single S3 generic
strucplot() function that is a wrapper for the Lattice package's xyplot()
function. This allows access to all Lattice graphics capabilities in the
usual way.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
