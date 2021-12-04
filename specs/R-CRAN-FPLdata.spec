%global __brp_check_rpaths %{nil}
%global packname  FPLdata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read in Fantasy Premier League Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-dplyr 

%description
This data contains a large variety of information on players and their
current attributes on Fantasy Premier League
<https://fantasy.premierleague.com/>. In particular, it contains a
`next_gw_points` (next gameweek points) value for each player given their
attributes in the current week. Rows represent player-gameweeks, i.e. for
each player there is a row for each gameweek. This makes the data suitable
for modelling a player's next gameweek points, given attributes such as
form, total points, and cost at the current gameweek. This data can
therefore be used to create Fantasy Premier League bots that may use a
machine learning algorithm and a linear programming solver (for example)
to return the best possible transfers and team to pick for each gameweek,
thereby fully automating the decision making process in Fantasy Premier
League. This function simply supplies the required data for such a task.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
