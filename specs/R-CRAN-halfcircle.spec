%global packname  halfcircle
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Plot Halfcircle Diagram

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-graphics 
Requires:         R-CRAN-scales 
Requires:         R-graphics 

%description
There are growing concerns on flow data in diverse fields including trade,
migration, knowledge diffusion, disease spread, and transportation. The
package is an effective visual support to learn the pattern of flow which
is called halfcircle diagram. The flow between two nodes placed on the
center line of a circle is represented using a half circle drawn from the
origin to the destination in a clockwise direction. Through changing the
order of nodes, the halfcircle diagram enables users to examine the
complex relationship between bidirectional flow and each potential
determinants. Furthermore, the halfmeancenter function, which calculates
(un) weighted mean center of half circles, makes the comparison easier.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
