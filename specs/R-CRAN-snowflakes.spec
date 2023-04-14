%global __brp_check_rpaths %{nil}
%global packname  snowflakes
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Random Snowflake Generator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch

%description
The function generates and plots random snowflakes. Each snowflake is
defined by a given diameter, width of the crystal, color, and random seed.
Snowflakes are plotted in such way that they always remain round, no
matter what the aspect ratio of the plot is. Snowflakes can be created
using transparent colors, which creates a more interesting, somewhat
realistic, image. Images of the snowflakes can be separately saved as svg
files and used in websites as static or animated images.

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
