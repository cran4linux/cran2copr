%global packname  IPDfromKM
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Map Digitized Survival Curves Back to Individual Patient Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-readbitmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-readbitmap 

%description
An implementation to reconstruct individual patient data from Kaplan-Meier
(K-M) survival curves, visualize and assess the accuracy of the
reconstruction, then perform secondary analysis on the reconstructed data.
We involve a simple function to extract the coordinates form the published
K-M curves. The function is developed based on Poisot T. ’s digitize
package (2011) <doi:10.32614/RJ-2011-004> . For more complex and tangled
together graphs, digitizing software, such as 'DigitizeIt' (for MAC or
windows) or 'ScanIt'(for windows) can be used to get the coordinates.
Additional information should also be involved to increase the accuracy,
like numbers of patients at risk (often reported at 5-10 time points under
the x-axis of the K-M graph), total number of patients, and total number
of events. The package implements the modified iterative K-M estimation
algorithm (modified-iKM) improved upon the approach proposed by Guyot
(2012) <doi:10.1186/1471-2288-12-9> with some modifications.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
