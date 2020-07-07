%global packname  dynaSpec
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Dynamic Spectrogram Visualizations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-NatureSounds 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-tuneR 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-CRAN-NatureSounds 
Requires:         R-CRAN-ggplot2 

%description
A set of tools to generate dynamic spectrogram visualizations in video
format.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
